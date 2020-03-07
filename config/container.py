from injector import Injector

from app.repository import TaskRepository
from app.service import TaskService
from config.db import Database

injector = Injector()

database = injector.get(Database)
task_repository = injector.get(TaskRepository)
task_service = injector.get(TaskService)
