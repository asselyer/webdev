import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import { TaskList } from 'src/app/models/task-list';
import { Task } from 'src/app/models/task';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/task_list/', {});
  }

  getTasks(task_list: TaskList): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_list/${task_list.id}/`, {});
  }
  getTask(tasks: Task): Promise<Task[]>{
    return this.get(`http://localhost:8000/api/tasks/${tasks.id}`, {});
  }

  createTaskList(name: any): Promise<TaskList> {
    return this.post('http://localhost:8000/api/task_list/', {
      name: name
    });
  }
  createTask(name: any, status: string): Promise<Task> {
    return this.post('http://localhost:8000/api/tasks', {
      name1: name,
      status: status
    });
  }

  updateTaskList(task_list: TaskList): Promise<TaskList> {
    return this.put(`http://localhost:8000/api/task_list/${task_list.id}/`, {
      name: task_list.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_list/${id}/`, {});
  }

  deleteTask(pk: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasks/${pk}/`, {});
  }
  


}
