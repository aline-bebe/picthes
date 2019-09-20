from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required, current_user
from .forms import UpdateProfile, PitchForm, CommentForm, CategoryForm
from .. import db, photos