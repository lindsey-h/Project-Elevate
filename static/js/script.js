"use strict";



$.get('/event-data', (data) => {

  $('#evoCalendar').evoCalendar({
    calendarEvents: data,
    todayHighlight: true,
    sidebarToggler: true,
    sidebarDisplayDefault: false,
  })

  .on('selectDate', function(newDate, oldDate) {
    $('#evoCalendar').removeClass('event-hide');
    $('#evoCalendar').addClass('sidebar-hide');
  })

  $('#sidebarToggler').on('click', () => {
    $('#evoCalendar').addClass('event-hide');
  })

  $('#eventListToggler').on('click', () => {
    $('#evoCalendar').addClass('sidebar-hide');
  })

});

// $('#evoCalendar').removeClass('sidebar-hide');
// $("#evoCalendar").evoCalendar('toggleSidebar',true/false);

// .on('click.evocalendar', _.toggleSidebar);

// .on('selectDate', function(newDate, oldDate) {
//   alert("I clicked a date");
// })
;

// // IF eventListToggler: set event listener: toggleEventList
// if(_.options.eventListToggler) {
//   _.$elements.eventListToggler
//   .off('click.evocalendar')
//   .on('click.evocalendar', _.toggleEventList);
// }
