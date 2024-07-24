import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MychoiceComponent } from './mychoice.component';

describe('MychoiceComponent', () => {
  let component: MychoiceComponent;
  let fixture: ComponentFixture<MychoiceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MychoiceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MychoiceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
