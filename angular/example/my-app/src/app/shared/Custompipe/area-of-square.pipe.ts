import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'areaOfSquare'
})
export class AreaOfSquarePipe implements PipeTransform {

  transform(value: any) {
    return value**2;
  }

}
