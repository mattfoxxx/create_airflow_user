#!/usr/bin/env python

import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

import click

@click.command()
@click.option('-u', '--username', prompt='User that should be created', help='The username for the new account')
@click.option('-p', '--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.option('-e', '--email', prompt='Email address for this user', help='The email address for the new account')
def create_user(username, password, email):
    """This programm creates users for airflow."""

    user = PasswordUser(models.User())
    user.username = username
    user.email = email
    user.password = password
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()
    click.echo(f'Account {username} created successfully!')

if __name__ == '__main__':
    create_user()

