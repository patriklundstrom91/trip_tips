const backButton = document.getElementById("btnBack");
/**
 * js for back button in confirm delete to go back one step 
 * to previous page since it can be trigger from different pages.
 */
if (backButton) {
    backButton.addEventListener("click", () => {
        history.back();
    });
}


const editButtons = document.getElementsByClassName("btn-comment-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-comment-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



/**
 * Adds edit functionality to edit button.
 * For each button in editButtons:
 * Retrieve comment's ID on click and fetch the comment.
 * Prepopulate the comment text-field with present comment.
 * Update button from submit to update.
 * Sets form action to edit_comment/{commentId} endpoint.
 * Done same way as I learned in walkthrough django blog project.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/**
 * Add delete functionality to delete button.
 * For each button in deleteButtons
 * Retrieve comment's ID on click.
 * Updates the deleteConfirm link's href to point to the 
 * deletion endpoint for the specific comment.
 * Display confirmation modal.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}