import {Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import { TaskList } from 'src/app/models/task-list';
import { Task } from 'src/app/models/task';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/task_list/', {});
  }

  getTaskListTasks(id: number): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_list/${id}/tasks/`, {});
  }

}