# Bugs

- UI

  - Stepper icon turns into a different color once left
  - Make the result boxes the same height
  - Is reset on fridge necessary, also each time your cancel something in fridge filter it automatically updates for you
  - Can't get search icon in fridge
  - Icons in fridge not included unlessly we make some breaking changes to the code we wrote in step 1
  - Some things are not responsive like the desc. in home page and the back button in empty your fridge frame
  - Highlight underneath the name of the recipe generated is inconsistent
  - Same as above, we would need to work some magic and have an intense code refactoring to get icons in step 3

- Frontend

  - For some of the recipes it times out cause it's too big
  - Substitutes are not replaced in recipe
  - Cuisine type filter not supported because it relies on description, and we would get no results most of the time
  - Also diet and cuisine type filter haven't been implemented yet
  - Weird bug where if you delete your ingredients in step 2, it's not synced in step 1
  - Choose your dishes hasn't been implemented yet

- Backend
  - Why can I not set a pagination limit on the number of substitutes

# If possible

# Potential features

# To do

- Infra-relatedish
  - push new docker images
  - Somehow get this out there, either do some magic with Trafeik and Docker Swarm or consider Dokku for backend
  - Otherwise docker-compose
  - Remember to chage ports when you use docker-compose, frontend needs to go to port 80 and not 8000
  - Build a new docker image [everytime](!https://docs.github.com/en/actions/guides/publishing-docker-images) backend changes?

# Advice

![](res/2021-04-22-10-53-53.png)

- ~~share, delaying this since we don't have a valid url, use [vue-social-sharing](!https://github.com/nicolasbeauvais/vue-social-sharing)~~, edit: we can't do this since we don't generate a link and Vue.js is mostly a client-side framework. Should've used Nuxt.js if we were to do this

- Cleaned up backend, something I should've done at the start

- Always use `created` hook for API calls instead of `mounted` since `created` happens before `mounted` and `mounted` happens when the DOM is rendered which doesn't matter for API calls.

- Avoid `position:absolute` if you don't have the parent component having a fixed height and width

- Secured backend with HTTPS 😎, this helped me a [lot](!https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)

- Never going to use npm as a package manager and virutal env for package management in python. From now on all my projects will be done in yarn and poetry respectively.

- I should've used Vuex and Typescript to begin with, Vuex would've helped me easily and safely manage state. Typescript would've saved me from wasted hours of debugging an undefined value which was the result of a property not existing :(
