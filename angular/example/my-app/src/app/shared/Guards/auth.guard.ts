import { CanActivateFn } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  
  if(typeof sessionStorage!=="undefined" && !!sessionStorage.getItem("user")){
   
    return true
  }
  return false
};
