from flask import Flask
from config import Config
from models import db
from controllers import list_markets, search_market, market_detail, delete_market

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return list_markets()

@app.route('/search')
def search():
    return search_market()

@app.route('/market/<int:fm_id>', methods=['GET', 'POST'])
def market(fm_id):
    return market_detail(fm_id)

@app.route('/market/<int:market_id>/delete', methods=['POST'])
def delete(market_id):
    return delete_market(market_id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)