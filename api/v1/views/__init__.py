from flask import Blueprint, render_template, redirect, url_for, request, flash
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
