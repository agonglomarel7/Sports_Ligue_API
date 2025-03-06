from flask import Flask, request
from db import ligues,teams
import uuid

app = Flask(__name__)


@app.get("/ligues")
def get_Sports():
    return {"Ligues List" : list(ligues.values())}

@app.post("/ligues/add_ligue")
def create_ligue():

    get_data = request.get_json()
    ligue_id = uuid.uuid4().hex
    new_ligue = {"id" : ligue_id, **get_data }
    ligues[ligue_id] = new_ligue
    return new_ligue, 200

@app.post("/ligues/add_ligue_teams/<string:name>/ligue_teams")
def create_team(name):

    get_request = request.get_json()

    for ligue in ligues:
        if ligue["ligue_name"]==name:
            new_team = {"team_name" : get_request["team_name"], "team_players":[]}
            ligue["ligue_teams"].append(new_team)

            return new_team, 200
    return {"Message Error":"Ligue doesn't exist."}, 404

@app.get("/ligues/<string:ligue_id>")
def get_ligues(ligue_id):
        
        try:
            return ligues[ligue_id]
        except KeyError:
            return {"Message error : " :"Not found"}, 404
    

@app.get("/ligues/<string:name>/team_info")
def get_team_info(name):

    for ligue in ligues:
        if ligue["ligue_name"] == name :

            return ligue["ligue_teams"]
        return {"Message error : " :"Not found"}, 404
