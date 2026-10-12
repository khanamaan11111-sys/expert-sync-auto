# Stage 6: publishing reviewed vehicle listings

The public catalogue reads listings.json. It starts with an empty listings array because no actual seller-approved vehicle data has been supplied.

Publication checklist:
1. Confirm the seller authorizes publication of the vehicle information and any images.
2. Check the price, vehicle details, and current availability with the seller.
3. Remove private seller phone numbers, home addresses, ID documents, and registration certificate numbers from public data.
4. Give each car a unique ID and add a record to the listings array in listings.json.
5. Set status to published, sellerPermissionConfirmed to true, and detailsReviewed to true only after completing those checks.
6. Commit the change and test inventory.html and its WhatsApp enquiry.
7. Remove or withdraw a record promptly if the vehicle is sold or no longer offered.

Use the Stage 4 listing-prep.html form to create a draft. A draft is not automatically published. Only authorized GitHub collaborators can edit the public inventory file. Do not publish invented vehicle records.

The static listing-prep.html page is not an authenticated admin dashboard. Do not enter sensitive information there.