import requests


# my_pizza_order = {
#     "customer" : "jon",
#     "custtel" : "2125655895",
#     "custemail" : "",
#     "size" : "small",
#     "topping" : "jalapeno",
#     "delivery" : "14:15",
#     "comments" : "Call me when you are here."
# }
# r = requests.post('http://httpbin.org/post', data = my_pizza_order)
#
# print(r.text)

contact_form_json = {
    "name" : "Shawn",
    "lastname" : "Rajput",
    "email" : "shawn.s.rajput@gmail.com",
    "message" : "Sending email for extra credit."
}
r = requests.post('https://lambdaschool.com/contact-form', json = contact_form_json)
print(r.status_code)
print(r.text)

# my_blog_post = {
#     "subject" : "How to learn anything",
#     "text" : "Could be anything.",
#     "comments_enabled" : True
# }
# r = requests.post('https://posttestserver.com/post.php', data = my_blog_post)
# print(r.text)
