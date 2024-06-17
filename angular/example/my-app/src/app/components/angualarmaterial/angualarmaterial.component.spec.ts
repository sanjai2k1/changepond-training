import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AngualarmaterialComponent } from './angualarmaterial.component';

describe('AngualarmaterialComponent', () => {
  let component: AngualarmaterialComponent;
  let fixture: ComponentFixture<AngualarmaterialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AngualarmaterialComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AngualarmaterialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
