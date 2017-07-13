
import webapp2
import logging
import os
import jinja2

jinja2_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
  def get(self):
     template = jinja2_environment.get_template('beatit.html')
     self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
