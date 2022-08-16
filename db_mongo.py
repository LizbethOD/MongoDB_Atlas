import web
import pymongo

urls = ('/', 'show_data')

conexion = pymongo.MongoClient("mongodb+srv://Liz:MongoLZ99@cluster0.amjcq1g.mongodb.net/?retryWrites=true&w=majority")
data_base = conexion.ExchangeMonedas

class show_data:
    def GET(self):
        coins = data_base.Monedas
        coin = coins.find()
        return coin

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()