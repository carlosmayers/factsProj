
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

class FaceShape(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('face_shape.html')
     self.response.write(template.render())

class EyeShape(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('eye_shape.html')
     self.response.write(template.render())

class BrowShape(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('brow_shape.html')
     self.response.write(template.render())

class EyeColor(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('eye_color.html')
     self.response.write(template.render())
class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))

class SkinType(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('skin_type.html')
     self.response.write(template.render())

class SkinTone(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('skin_tone.html')
     self.response.write(template.render())

class LipsHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja2_environment.get_template('lips.html')
     self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/faceshape', FaceShape),
    ('/eyeshape', EyeShape),
    ('/browshape', BrowShape),
    ('/eyecolor', EyeColor),
    ('/skintype', SkinType),
    ('/skintone', SkinTone),
    ('/lips', LipsHandler)
], debug=True)
