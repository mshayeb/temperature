'''
    Filename:
        TemperatureWebServiceServer.py

    Description:
        Server for temperature conversion web service on localhost
'''

##################################################################
# ignore warnings 
##################################################################
import warnings
from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)


from flask import Flask, jsonify
from flask_restful import Api, Resource, abort
import logging

app = Flask(__name__)
api = Api(app)

##################################################################
# class for Converting to Fahrenheit
##################################################################
class ConvertFahrenheit(Resource):
    '''
    get method used by Restful to return conversions
    exception if the value is not float or int
    @param temp: temperature needs to convert
    @return: conversion of a temperature as json
    '''
    def get(self,temp):
        try:
            return {
                'kelvin': ((float(temp)+459.67)*(5.0/9.0)), 
                'rankine': (float(temp)+459.67), 
                'celsius': ((float(temp)-32)/1.8)
            }
        except ValueError:
            app.logger.error('Wrong input format')
            abort(400, message="Input must be float or Int")

##################################################################
# class for Converting to Celsius
##################################################################
class ConvertCelsius(Resource):
    '''
    get method used by Restful to return conversions
    exception if the value is not float or int
    @param temp: temperature needs to convert
    @return: conversion of a temperature as json
    '''
    def get(self,temp):
        try:
            return {
                'kelvin': (float(temp)+273.15), 
                'rankine': ((float(temp)+273.15)*(9.0/5.0)), 
                'fahrenheit': ((float(temp)*1.8)+32)
            }
        except ValueError:
            app.logger.error('Wrong input format')
            abort(400, message="Input must be float or Int")

##################################################################
# class for Converting to Fahrenheit
##################################################################            
class ConvertKelvin(Resource):
    '''
    get method used by Restful to return conversions
    exception if the value is not float or int
    @param temp: temperature needs to convert
    @return: conversion of a temperature as json
    '''
    def get(self,temp):
        try:
            return {
                'celsius': (float(temp)-273.15), 
                'rankine': (float(temp)*(9.0/5.0)), 
                'fahrenheit': ((float(temp)*(9.0/5.0))-459.67)
            }
        except ValueError:
            app.logger.error('Wrong input format')
            abort(400, message="Input must be float or Int")
            
##################################################################
# class for Converting to Fahrenheit
##################################################################            
class ConvertRankine(Resource):
    '''
    get method used by Restful to return conversions
    exception if the value is not float or int
    @param temp: temperature needs to convert
    @return: conversion of a temperature as json
    '''
    def get(self,temp):
        try:
            return {
                'celsius': ((float(temp)-491.67) * (5.0/9.0)), 
                'Kelvin': (float(temp)*(5.0/9.0)), 
                'fahrenheit': (float(temp)-459.67)
            }
        except ValueError:
            app.logger.error('Wrong input format')
            abort(400, message="Input must be float or Int")

'''
endpoint for every class to convert temperature            
'''
api.add_resource(ConvertFahrenheit, '/convert/fahrenheit/<temp>', '/convert/fahrenheit/<temp>/',endpoint='/convert/fahrenheit')
api.add_resource(ConvertCelsius, '/convert/celsius/<temp>', '/convert/celsius/<temp>/',endpoint='/convert/celsius')
api.add_resource(ConvertKelvin, '/convert/kelvin/<temp>', '/convert/kelvin/<temp>/',endpoint='/convert/kelvin')
api.add_resource(ConvertRankine, '/convert/rankine/<temp>', '/convert/rankine/<temp>/',endpoint='/convert/rankine')

'''
run server in debug mode
'''
if __name__ == '__main__':
    app.run(debug=True)
