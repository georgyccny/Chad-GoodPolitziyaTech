import os
from flask import Flask, request, redirect, jsonify, abort, make_response, Response, send_file, session
from flask_restful import Resource, Api,reqparse
import requests
import json


api_route = 'http://127.0.0.1:8001'


def add_user_to_db(username, password, user_type):
    body = {'username': username, "password": password, "user_type": user_type}
    req_url = f'{api_route}/user/add'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data

def get_user_from_db(username):
    body = {'username': username}
    req_url = f'{api_route}/user/get'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data


def update_user_in_db(username, attribute, value):
    body = {'username': username, 'attribute': attribute, 'value': value}
    req_url = f'{api_route}/user/update'
    r = requests.post(req_url, json=body)
    r_json = r.json()
    try:
        data = r_json['info']
    except:
        data = r_json['error']
    return data

# a = add_user_to_db('Alex', '123', 'admin')
# print(a)

# b = get_user_from_db('georgy')
# print(b)

c = update_user_in_db('georgy', 'compliments', 1)
print(c)