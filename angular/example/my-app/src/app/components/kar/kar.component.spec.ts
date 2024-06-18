import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KarComponent } from './kar.component';

describe('KarComponent', () => {
  let component: KarComponent;
  let fixture: ComponentFixture<KarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [KarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
