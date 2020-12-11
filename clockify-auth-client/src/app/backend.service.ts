import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  // backend_url = "http://127.0.0.1:5000/"
  backend_url = "https://1t12wkqcf5.execute-api.eu-central-1.amazonaws.com/HACK/clockify-auth-server"

  constructor(private http: HttpClient) { }

  validate(user_token: string, user_api_key: string): Observable<any>  {

    let body = { "user_token": user_token, "user_api_key": user_api_key };
    return this.http.post<any>(this.backend_url, body);
  }

}
