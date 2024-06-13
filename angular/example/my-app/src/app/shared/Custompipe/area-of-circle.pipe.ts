import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'areaOfCircle'
})
export class AreaOfCirclePipe implements PipeTransform {

  transform(value:any) {
    return 3.14*(value**2);
  }

}
