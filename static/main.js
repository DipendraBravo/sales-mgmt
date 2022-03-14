function showModel(id){
    $('#book_id').val(id)
    console.log($("#book_id").val())
    $('#buy').modal('show');
    // $('#byform').attr('action',`/buy/${id}`)


}