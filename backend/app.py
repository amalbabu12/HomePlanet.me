"""
Initial server file.
"""
import json
import random

import flask
import flask_cors
from flask import request

import utils

HOST = "0.0.0.0"
PORT = 8000

app: flask.Flask = flask.Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)

error_header = {"Content-Type": "text/plain"}
return_header = {"Content-Type": "application/json"}


def searchFunction(query: str, object: dict):
    for key in object:
        if isinstance(object[key], str) and query.lower() in object[key].lower():
            return True
    return False


@app.route("/api", methods=["GET"])
def index() -> str:
    """
    This api is just used for test. :)
    ret:    `str`, a welcome string
    """
    return "Hello, welcome to homeplanet.me!"


@app.route("/api/all_moons", methods=["GET"])
def api_all_moons():
    """
    This api returns all information on the moon.
    ret:    `json`, related information on the assigned moon
            `status_code`, the status code of this reply
    """
    page: str = request.args.get("page")
    per_page: str = request.args.get("per_page")
    sort_index: str = request.args.get("sort-index")
    sort_english_name: str = request.args.get("sort-english-name")
    sort_density: str = request.args.get("sort-density")
    sort_gravity: str = request.args.get("sort-gravity")
    sort_around_planet: str = request.args.get("sort-around-planet")
    sort_mass_value: str = request.args.get("sort-mass-value")
    sort_mass_exponent: str = request.args.get("sort-mass-exponent")
    sort_vol_value: str = request.args.get("sort-vol-value")
    sort_vol_exponent: str = request.args.get("sort-vol-exponent")
    sort_discovery_date: str = request.args.get("sort-discovery-date")
    search_val: str = request.args.get("search")

    filter_planet: str = request.args.get("filter")


    moons: list[dict] = utils.get_moons()

    if filter_planet is not None:
        filter_planet = "terre" if filter_planet.lower() == 'earth' else filter_planet.lower()


        moons = list(filter(
        lambda x: filter_planet in x["aroundPlanet"].lower(),
        moons
    ))

    if search_val is not None:
        search_val = search_val.lower()
        moons = list(filter(
            lambda x:  search_val in x["englishName"].lower() 
            or search_val in x["aroundPlanet"].lower(),
            moons
        ))

    if sort_index:
        moons = sorted(moons, key=lambda moon: moon["index"])
    elif sort_english_name:
        moons = sorted(moons, key=lambda moon: moon["englishName"])
    elif sort_density:
        moons = sorted(moons, key=lambda moon: moon["density"])
    elif sort_gravity:
        moons = sorted(moons, key=lambda moon: moon["gravity"])
    elif sort_around_planet:
        moons = sorted(moons, key=lambda moon: moon["aroundPlanet"])
    elif sort_mass_value:
        moons = sorted(moons, key=lambda moon: moon["massValue"])
    elif sort_mass_exponent:
        moons = sorted(moons, key=lambda moon: moon["massExponent"])
    elif sort_vol_value:
        moons = sorted(moons, key=lambda moon: moon["volValue"])
    elif sort_vol_exponent:
        moons = sorted(moons, key=lambda moon: moon["volExponent"])
    elif sort_discovery_date:
        moons = sorted(moons, key=lambda moon: moon["discoveryDate"])

    if page is None or per_page is None or len(page) == 0 or len(per_page) == 0:
        moons_slice: list[dict] = moons
    else:
        page: int = int(page)
        per_page: int = int(per_page)
        moons_slice: list[dict] = moons[(page - 1) * per_page : page * per_page]

    ret: dict = {
        "size": len(moons_slice),
        "total_size": len(moons),
        "bodies": moons_slice,
    }
    return json.dumps(ret), 200, return_header


@app.route("/api/all_planets", methods=["GET"])
def api_all_planets():
    """
    This api returns all information on the planet.
    ret:    `json`, related information on the assigned planet
            `status_code`, the status code of this reply
    """
    page: str = request.args.get("page")
    per_page: str = request.args.get("per_page")
    sort_index: str = request.args.get("sort-index")
    sort_pl_name: str = request.args.get("sort-pl-name")
    sort_hostname: str = request.args.get("sort-hostname")
    sort_pl_masse: str = request.args.get("sort-pl-masse")
    sort_pl_rade: str = request.args.get("sort-pl-rade")
    sort_pl_dens: str = request.args.get("sort-pl-dens")
    sort_pl_eqt: str = request.args.get("sort-pl-eqt")
    sort_pl_orbper: str = request.args.get("sort-pl-orbper")
    search_val: str = request.args.get("search")


    filter_temp: str = request.args.get("filter")

    planets: list[dict] = utils.get_planets()

    if filter_temp is not None:
        filter_temp = filter_temp.lower()
        lower, upper = utils.HABITABLE
        if filter_temp == 'too-cold':
            planets = list(filter(
                lambda x: x['pl_eqt'] < lower,
                planets
            ))
        elif filter_temp == 'habitable':
            planets = list(filter(
                lambda x: lower <= x['pl_eqt'] <= upper,
                planets
            ))

        else:
            planets = list(filter(
                lambda x:  x['pl_eqt'] > upper,
                planets
            ))

    if search_val is not None:
        search_val = search_val.lower()
        planets = list(filter(
            lambda x:  search_val in x["pl_name"].lower() 
            or search_val in x["hostname"].lower(),
            planets
        ))

    if sort_index:
        planets = sorted(planets, key=lambda planet: planet["index"])
    elif sort_pl_name:
        planets = sorted(planets, key=lambda planet: planet["pl_name"])
    elif sort_hostname:
        planets = sorted(planets, key=lambda planet: planet["hostname"])
    elif sort_pl_masse:
        planets = sorted(planets, key=lambda planet: planet["pl_masse"])
    elif sort_pl_rade:
        planets = sorted(planets, key=lambda planet: planet["pl_rade"])
    elif sort_pl_dens:
        planets = sorted(planets, key=lambda planet: planet["pl_dens"])
    elif sort_pl_eqt:
        planets = sorted(planets, key=lambda planet: planet["pl_eqt"])
    elif sort_pl_orbper:
        planets = sorted(planets, key=lambda planet: planet["pl_orbper"])

    if page is None or per_page is None or len(page) == 0 or len(per_page) == 0:
        planets_slice: list[dict] = planets
    else:
        page: int = int(page)
        per_page: int = int(per_page)
        planets_slice: list[dict] = planets[(page - 1) * per_page : page * per_page]
    ret: dict = {
        "size": len(planets_slice),
        "total_size": len(planets),
        "bodies": planets_slice,
    }
    return json.dumps(ret), 200, return_header


@app.route("/api/all_stars", methods=["GET"])
def api_all_stars():
    """
    This api returns all information on the star.
    ret:    `json`, related information on the assigned star
            `status_code`, the status code of this reply
    """
    page: str = request.args.get("page")
    per_page: str = request.args.get("per_page")
    sort_index: str = request.args.get("sort-index")
    sort_star_name: str = request.args.get("sort-star-name")
    sort_st_teff: str = request.args.get("sort-st-teff")
    sort_st_lumclass: str = request.args.get("sort-st-lumclass")
    sort_st_age: str = request.args.get("sort-st-age")
    sort_st_rad: str = request.args.get("sort-st-rad")
    sort_st_mass: str = request.args.get("sort-st-mass")
    sort_st_logg: str = request.args.get("sort-st-logg")
    sort_color: str = request.args.get("sort-color")
    search_val: str = request.args.get("search")

    filter_class: str = request.args.get("filter")

    stars: list[dict] = utils.get_stars()

    if filter_class is not None:
        filter_class = filter_class.lower()

        stars = list(filter(
            lambda x: filter_class in x['st_lumclass'].lower(),
            stars
        ))

    if search_val is not None:
        search_val = search_val.lower()
        stars = list(filter(
            lambda x:  search_val in x["star_name"].lower() 
            or search_val in x["st_lumclass"].lower()
            or search_val in x["color"].lower(),
            stars
        ))

    if sort_index:
        stars = sorted(stars, key=lambda star: star["index"])
    elif sort_star_name:
        stars = sorted(stars, key=lambda star: star["star_name"])
    elif sort_st_teff:
        stars = sorted(stars, key=lambda star: star["st_teff"])
    elif sort_st_lumclass:
        stars = sorted(stars, key=lambda star: star["st_lumclass"])
    elif sort_st_age:
        stars = sorted(stars, key=lambda star: star["st_age"])
    elif sort_st_rad:
        stars = sorted(stars, key=lambda star: star["st_rad"])
    elif sort_st_mass:
        stars = sorted(stars, key=lambda star: star["st_mass"])
    elif sort_st_logg:
        stars = sorted(stars, key=lambda star: star["st_logg"])
    elif sort_color:
        stars = sorted(stars, key=lambda star: star["color"])

    if page is None or per_page is None or len(page) == 0 or len(per_page) == 0:
        stars_slice: list[dict] = stars
    else:
        page: int = int(page)
        per_page: int = int(per_page)
        stars_slice: list[dict] = stars[(page - 1) * per_page : page * per_page]

    ret: dict = {
        "size": len(stars_slice),
        "total_size": len(stars),
        "bodies": stars_slice,
    }
    return json.dumps(ret), 200, return_header


@app.route("/api/moon", methods=["GET"])
def api_moon():
    """
    This api returns all information on the assigned moon.
    ret:    `json`, related information on the assigned moon
            `status_code`, the status code of this reply
    """
    index: str = request.args.get("index")
    name: str = request.args.get("name")
    if not index and not name:
        return (
            'Cannot find argument "index" or "name". Please check your request.',
            404,
            error_header,
        )
    elif index and name:
        return (
            'Cannot get argument "index" and "name" at the same time. Please check your request.',
            404,
            error_header,
        )
    if index:
        index = int(index)
        moon = utils.get_moon_by_index(index)
    elif name:
        moon = utils.get_moon_by_name(name)
    return json.dumps(moon), 200, return_header


@app.route("/api/planet", methods=["GET"])
def api_planet():
    """
    This api returns all information on the assigned planet.
    ret:    `json`, related information on the assigned planet
            `status_code`, the status code of this reply
    """
    index: str = request.args.get("index")
    name: str = request.args.get("name")
    if not index and not name:
        return (
            'Cannot find argument "index" or "name". Please check your request.',
            404,
            error_header,
        )
    elif index and name:
        return (
            'Cannot get argument "index" and "name" at the same time. Please check your request.',
            404,
            error_header,
        )
    if index:
        index = int(index)
        planet = utils.get_planet_by_index(index)
    elif name:
        planet = utils.get_planet_by_name(name)
    return json.dumps(planet), 200, return_header


@app.route("/api/star", methods=["GET"])
def api_star():
    """
    This api returns all information on the assigned star.
    ret:    `json`, related information on the assigned star
            `status_code`, the status code of this reply
    """
    index: str = request.args.get("index")
    name: str = request.args.get("name")
    if not index and not name:
        return (
            'Cannot find argument "index" or "name". Please check your request.',
            404,
            error_header,
        )
    elif index and name:
        return (
            'Cannot get argument "index" and "name" at the same time. Please check your request.',
            404,
            error_header,
        )
    if index:
        index = int(index)
        star = utils.get_star_by_index(index)
    elif name:
        star = utils.get_star_by_name(name)
    return json.dumps(star), 200, return_header


@app.route("/api/recommend/moon", methods=["GET"])
def recommend_moon():
    """
    This api returns recommendations based on the moon. For the moon it returns a random star
     and a random planet.
    ret:    `json`, the basic information of recommended star and planet
            `status_code`, the status code of this reply
    """
    moon: str = request.args.get("moon")
    if not moon:
        return (
            'Cannot find argument "moon". Please check your request.',
            404,
            error_header,
        )
    star: dict = random.choice(utils.get_stars())
    planet: dict = random.choice(utils.get_planets())
    ret: dict = {"star": star, "planet": planet}
    return json.dumps(ret), 200, return_header


@app.route("/api/recommend/planet", methods=["GET"])
def recommend_planets():
    """
    This api returns recommendations based on the planet. For the planet, it searches for an
     available star and randomly recommends a moon based on the galaxy it is in.
    ret:    `json`, the basic information of recommended star and moon
            `status_code`, the status code of this reply
    """
    planetIndex: str = request.args.get("planet")

    if not planetIndex:
        return (
            'Cannot find argument "planet". Please check your request.',
            404,
            error_header,
        )
    hostname: dict = utils.get_planet_by_index(planetIndex)[0]["hostname"]
    star: dict = utils.get_star_by_name(hostname)
    planetIndex = str(int(planetIndex) % 150)
    if not star:
        star = utils.get_star_by_index(planetIndex)
    moon: dict = utils.get_moon_by_index(planetIndex)
    ret: dict = {"star": star, "moon": moon}
    return json.dumps(ret), 200, return_header


@app.route("/api/recommend/star", methods=["GET"])
def recommend_stars():
    """
    This api returns recommendations based on the star. For the star, it searches for planets in
     the same galaxy and randomly recommends moons.
    ret:    `json`, the basic information of recommended planet and moon
            `status_code`, the status code of this reply
    """
    starIndex: str = request.args.get("star")
    if not starIndex:
        return (
            'Cannot find argument "star". Please check your request.',
            404,
            error_header,
        )
    starName = utils.get_star_by_index(starIndex)[0]["star_name"]
    starIndex = str(int(starIndex) % 100)
    planet: dict = utils.get_planet_by_name(starName)
    if len(planet) == 0:
        planet = utils.get_planet_by_index(starIndex)
    
    moon: dict = utils.get_moon_by_index(starIndex)
    ret: dict = {"planet": planet, "moon": moon}
    return json.dumps(ret), 200, return_header


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
