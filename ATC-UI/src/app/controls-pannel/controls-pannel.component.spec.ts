import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ControlsPannelComponent } from './controls-pannel.component';

describe('ControlsPannelComponent', () => {
  let component: ControlsPannelComponent;
  let fixture: ComponentFixture<ControlsPannelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ControlsPannelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ControlsPannelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
