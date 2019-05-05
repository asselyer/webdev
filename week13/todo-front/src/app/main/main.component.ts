import { Component,Input, OnDestroy, OnInit } from '@angular/core';
import { TaskList } from 'src/app/task-list';
import { Task } from 'src/app/task';
import { ProviderService } from 'src/app/services/provider.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public output = '';
  public stringArray: string[] = [];

  public tasklists: TaskList[] = [];
  public loading = false;

  public tasks: Task[] = [];

  public name: any = '';

  public isLogged = false;

  public login = '';
  public password = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if (this.isLogged) {
      this.getTaskLists();
    }

  }

  getTaskLists() {
    this.provider.getTaskLists().then(res => {
      this.tasklists = res;
      this.loading = true;
    });
  }

  getTasks(task_list: TaskList) {
    this.provider.getTasks(task_list).then(res => {
      this.tasks = res;
    });
  }

  sendMessageByService() {
    this.provider.sendMessage.emit('This message From Parent Component');
  }

  updateTaskList(l: TaskList) {
    this.provider.updateTaskList(l).then(res => {
      console.log(l.name + ' updated');
    });
  }

  deleteTaskList(l: TaskList) {
    this.provider.deleteTaskList(l.id).then(res => {
      console.log(l.name + ' deleted');
      this.provider.getTaskLists().then(r => {
        this.tasklists = r;
      });
    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.tasklists.push(res);
      });
    }
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTaskLists();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }

}