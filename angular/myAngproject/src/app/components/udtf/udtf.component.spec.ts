import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UdtfComponent } from './udtf.component';

describe('UdtfComponent', () => {
  let component: UdtfComponent;
  let fixture: ComponentFixture<UdtfComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UdtfComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UdtfComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
