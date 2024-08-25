import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecomendationsComponent } from './recomendations.component';

describe('RecomendationsComponent', () => {
  let component: RecomendationsComponent;
  let fixture: ComponentFixture<RecomendationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecomendationsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RecomendationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
