
import bottle
import model


vislice = model.Vislice()

@bottle.get("/")
def prikazi_osnovno_stran():
    return bottle.template("index")