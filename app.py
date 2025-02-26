from flask import Flask, request


app = Flask(__name__)

ligues = [
    {
        "ligue_name" : "PL",
        "ligue_teams" : [
            {
                "team_name" : "Arsenal FC",
                "team_players" : [
                    {
                        "player_name":"BOUKAYO SAKA",
                        "player_nationality": "Nigeria-England"

                    }
                ]
            }
        ]
               
    },
        {
        "ligue_name" : "BBVA",
        "ligue_teams" : [
            {
                "team_name" : "Barcelona FC",
                "team_players" : [
                    {
                        "player_name":"Lamine YAMAL",
                        "player_nationality": "Morrocco-Spain"

                    }
                ]
            }
        ]
               
    }
]

@app.get("/ligues")
def get_Sports():

    return {"Ligues List" : ligues}

@app.post("/ligues/add_ligue")
def create_ligue():

    get_request = request.get_json()
    new_ligue = {"ligue_name" : get_request["ligue_name"], "ligue_teams" : []}
    ligues.append(new_ligue)
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

@app.get("/ligues/<string:name>")
def get_ligues(name):

    for ligue in ligues:
        if ligue["ligue_name"] == name :

            return  ligue
        return {"Message error : " :"Not found"}, 404
    

@app.get("/ligues/<string:name>/team_info")
def get_team_info(name):

    for ligue in ligues:
        if ligue["ligue_name"] == name :

            return ligue["ligue_teams"]
        return {"Message error : " :"Not found"}, 404
