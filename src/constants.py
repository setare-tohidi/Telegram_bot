# Simple name space: calling dictionaries with keys
from types import SimpleNamespace
from telebot import types


keys=SimpleNamespace(
    random_connect='Random Connect',
    settings='Settings')

keyboards=SimpleNamespace(main=create_keybaord(keys.random_connect, keys.settings))
