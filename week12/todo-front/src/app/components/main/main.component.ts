import { Component, OnInit, OnDestroy, EventEmitter, Input, Output } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';
import { TaskList } from 'src/app/models/task-list';
import { Task } from 'src/app/models/task';


@Component({
  selector: 'main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit  {

  public output = '';
  public stringArray: string[] = [];

  public tasklists: TaskList[] = [];
  public loading = false;

  public tasks: Task[] = [];

  public name: any = '';
  public status: any = '';
  public name1: any = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {

    this.provider.getTaskLists().then(res => {
      this.tasklists = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
    
  }
  

  getTasks(task_list: TaskList) {
    this.provider.getTasks(task_list).then(res => {
      this.tasks = res;
    });
  }
  getTask(tasks: Task) {
    this.provider.getTasks(tasks).then(res => {
      this.tasks = res;
    });
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

  deleteTask(t: Task) {
    this.provider.deleteTask(t.id).then(res => {
      console.log(t.name + ' deleted');
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

  
}