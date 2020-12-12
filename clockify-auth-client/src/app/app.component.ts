import { ChangeDetectorRef, Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BackendService } from './backend.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  title = 'clockify-auth-client';

  user_token: string;
  user_api_key: string;
  user_info_accepted: boolean;
  alert_msg: string;

  warning_flag: boolean = false;
  success_flag: boolean = false;
  error_flag: boolean = false;

  constructor( private route: ActivatedRoute,
               private backendService: BackendService,
               private ref: ChangeDetectorRef ) {
                this.route.queryParams.subscribe(params => {
                  this.user_token = params['user_token'];
                });
              }

  send_data(): void {
    this.warning_flag = false;
    this.success_flag = false;
    this.error_flag = false;

    if (this.user_info_accepted){
      if (this.user_token && this.user_token.trim() != ''){
      
        if (this.user_api_key && this.user_api_key.trim() != ''){

          this.backendService.validate(this.user_token,this.user_api_key).subscribe(
            (data: any) => {
              console.log(data.valid);
              if(data.valid){
                this.success_flag = true;
                this.alert_msg = "Worked! Try the Skill again.";
              } else{
                this.error_flag = true;
                this.alert_msg = "User Token and/or Clockify API key is not valid.";
              }
              this.ref.detectChanges();
          });
            
        } else {
          this.warning_flag = true;
          this.alert_msg = "Please enter you Clockify API key.";
        }
      } else {
        this.warning_flag = true;
        this.alert_msg = "Please enter you User Token from the Hallo Magenta APP Verlauf.";
      }
    } else {
      this.warning_flag = true;
      this.alert_msg = "Please agree that you just use a test account.";
    }
  }
}
