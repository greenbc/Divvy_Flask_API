from takehome_api import app, db

class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key = True)
    starttime = db.Column(db.String(150))
    stoptime = db.Column(db.String(150))
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String(300))
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String(300))
    usertype = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    birthday = db.Column(db.String(150))
    trip_duration = db.Column(db.Integer)

    def __init__(self,trip_id,starttime,stoptime,bikeid,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthday,trip_duration):
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration

    def __repr__(self):
        return f'{self.trip_duration}'

    def to_dict(self):
        return {
            "trip_id": self.trip_id,
            "starttime": self.starttime,
            "stoptime": self.stoptime,
            "bikeid": self.bikeid,
            "from_station_id": self.from_station_id,
            "from_station_name": self.from_station_name,
            "to_station_id": self.to_station_id,
            "to_station_name": self.to_station_name,
            "usertype": self.usertype,
            "gender": self.gender,
            "birthday": self.birthday,
            "trip_duration": self.trip_duration
        }