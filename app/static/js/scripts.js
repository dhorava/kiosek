/*!
    * Start Bootstrap - SB Admin v6.0.0 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    (function($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });


    $(document).ready( function() {
      $('#forecasty').DataTable({
          paging: true,
          "order": [[0, "desc"]]
      });
    });

    $(document).ready(function() {
      // Setup - add a text input to each footer cell
      $('#systemy thead tr').clone(true).appendTo( '#systemy thead' );
      $('#systemy thead tr:eq(1) th').each( function (i) {
          var title = $(this).text();
          $(this).html( '<input type="text" placeholder="Hledat v: '+title+'" />' );

          $( 'input', this ).on( 'keyup change', function () {
              if ( table.column(i).search() !== this.value ) {
                  table
                      .column(i)
                      .search( this.value )
                      .draw();
              }
          } );
      } );

      var table = $('#systemy').DataTable( {
          orderCellsTop: true,
          fixedHeader: true,
          paging: true,
          "order": [[2, "asc"], [0, "asc"]]
        });
    });


    $(document).ready(function() {
      var table = $('#nesystemy').DataTable();

      buildSelect( table );
      table.on( 'draw', function () {
        buildSelect( table );
      } );

    });


  function buildSelect( table ) {
    table.columns().every( function () {
      var column = table.column( this, {search: 'applied'} );
      var select = $('<select><option value=""></option></select>')
      .appendTo( $(column.footer()).empty() )
      .on( 'change', function () {
        var val = $.fn.dataTable.util.escapeRegex(
          $(this).val()
        );

        column
        .search( val ? '^'+val+'$' : '', true, false )
        .draw();
      } );

      column.data().unique().sort().each( function ( d, j ) {
        select.append( '<option value="'+d+'">'+d+'</option>' );
      } );

      // The rebuild will clear the exisiting select, so it needs to be repopulated
      var currSearch = column.search();
      if ( currSearch ) {
        select.val( currSearch.substring(1, currSearch.length-1) );
      }
    } );
  }

})(jQuery);
