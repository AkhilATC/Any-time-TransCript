import { Component, OnInit } from '@angular/core';
import { VoiceRecognitionService } from '../service/voice-recognition.service';

@Component({
  selector: 'app-controls-pannel',
  templateUrl: './controls-pannel.component.html',
  styleUrls: ['./controls-pannel.component.scss'],
  providers:[VoiceRecognitionService]
})
export class ControlsPannelComponent implements OnInit {

  constructor(public service: VoiceRecognitionService) { this.service.init()  }

  public isMicOn = false;
  public micText =  '🎙️' ;

  ngOnInit(): void {
  }
  captureVoice(){
    if(!this.isMicOn)
    { 
     this.service.start();
     this.isMicOn = true;
    }else{
      this.service.stop()
      this.isMicOn = false
    }
  }
  stopCapture(){
    this.service.stop()
    this.isMicOn = false

  }
}
