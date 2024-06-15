from flask import render_template, redirect, url_for, request
from models import db, Market, Review
from forms import ReviewForm

def list_markets():
    markets = Market.query.all()
    return render_template('index.html', markets=markets)

def search_market():
    query = request.args.get('query')
    markets = Market.query.filter(
        (Market.city.ilike(f'%{query}%')) |
        (Market.state.ilike(f'%{query}%')) |
        (Market.zip.ilike(f'%{query}%'))
    ).all()
    return render_template('index.html', markets=markets)

def market_detail(market_id):
    market = Market.query.get_or_404(market_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(
            user_nickname=form.user_nickname.data,
            text=form.text.data,
            rating=form.rating.data,
            fm_id=market.fm_id
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('market_detail', market_id=market.fm_id))
    return render_template('market_detail.html', market=market, form=form)

def delete_market(market_id):
    market = Market.query.get_or_404(market_id)
    db.session.delete(market)
    db.session.commit()
    return redirect(url_for('index'))