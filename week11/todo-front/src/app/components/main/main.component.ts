import { Component, OnInit, OnDestroy, EventEmitter, Input, Output } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';
import { TaskList } from 'src/app/models/task-list';
import { Task } from 'src/app/models/task';


@Component({
  selector: 'main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit, OnDestroy  {

  
  public subTitle = '';
  public array2: any[] = [];

  public tasklists: TaskList[] = [];
  public loading = false;

  public interval;
  public i = 0;

  public tasks: Task[] = [];
  


  constructor(private provider: ProviderService) { }

  ngOnInit() {

    this.provider.getTaskLists().then(res => {
      this.tasklists = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });

  }

  getTasks(tasklist: TaskList) {
    this.provider.getTaskListTasks(tasklist.id).then(res => {
      this.tasks = res;
    });
  }

  ngOnDestroy() {
    clearInterval(this.interval);
  }

}