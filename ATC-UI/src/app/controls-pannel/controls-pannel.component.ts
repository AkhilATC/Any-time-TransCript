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

  ngOnInit(): void {
  }
  captureVoice(){
    this.service.start();
  }
  stopCapture(){
    this.service.stop()

  }
}
