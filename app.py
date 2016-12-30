# Run Script
import os
os.system("played.py 1")

# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('played.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    from played import festbyyear
    from played import makefestvars
    from played import intersect
    from played import match_fest
    fest1=request.form['fest1']
    fest2=request.form['fest2']
    year=request.form['year']
    infotype=request.form['infotype']
    if infotype == 'who_played':
        return render_template('played_submit.html', fest1name=match_fest(fest1), fest1=fest1, festbands1=str(makefestvars(fest1).unique()), infotype=infotype)
    elif infotype == 'who_played_year':
        return render_template('played_submit.html', fest1name=match_fest(fest1), fest1=fest1, festyear=str(festbyyear(fest1, int(year)).unique()), year=year, infotype=infotype)
    elif infotype == 'overlap_bands':
        return render_template('played_submit.html', fest1name=match_fest(fest1), fest1=fest1, fest2name=match_fest(fest2), fest2=fest2, year=year, festbands1=str(makefestvars(fest1).unique()), 
                               festbands2=str(makefestvars(fest2).unique()), overlap=intersect(list(makefestvars(fest1)), list(makefestvars(fest2))), infotype=infotype, length=len(intersect(list(makefestvars(fest1)), list(makefestvars(fest2)))))
    elif infotype == 'overlap_bands_year':
        return render_template('played_submit.html', fest1name=match_fest(fest1), fest1=fest1, fest2name=match_fest(fest2), fest2=fest2, year=year, festbands1=str(makefestvars(fest1).unique()), 
                               festbands2=str(makefestvars(fest2).unique()), overlapyear=intersect(list(festbyyear(fest1, int(year))), list(festbyyear(fest2, int(year)))), infotype=infotype, 
							   lengthyear=len(intersect(list(festbyyear(fest1, int(year))), list(festbyyear(fest2, int(year))))))
    
# Run the app :)
if __name__ == '__main__':
  app.run()