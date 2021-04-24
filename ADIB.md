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

  - Will the user go back to step 1 to change their selection?
  - How do I add what the user selected already?
  - For some of the recipes it times out cause it's too big
  - When we remove an ingredient the recipe doesn't update

- Backend
  - Why can I not set a pagination limit on the number of substitutes

# If possible

- Frontend
  - Portions, if current implementation is fast we will add this later on
  - Tests
  - Add crosses for choose ingredients
  - **Change volumes and recipe if ingredient has been substituted**

# Potential features

- Download, I think we need an actual url for this, puppeteer
- Portions
- Substitutable ingredient changes recipe

# To do

- Frontend

  - Implement filter functionality, after Davis completes it
  - cache step 2

- Backend

  - Add testing to backend

- Infra-relatedish
  - Somehow get this out there, either do some magic with Trafeik and Docker Swarm or consider Dokku for backend
  - Otherwise docker-compose
  - Remember to chage ports when you use docker-compose, frontend needs to go to port 80 and not 8000

# Advice

![](res/2021-04-22-10-53-53.png)

- ~~share, delaying this since we don't have a valid url, use [vue-social-sharing](!https://github.com/nicolasbeauvais/vue-social-sharing)~~, edit: we can't do this since we don't generate a link and Vue.js is mostly a client-side framework. Should've used Nuxt.js if we were to do this

- Cleaned up backend, something I should've done at the start

- Always use `created` hook for API calls instead of `mounted` since `created` happens before `mounted` and `mounted` happens when the DOM is rendered which doesn't matter for API calls.

- Avoid `position:absolute` if you don't have the parent component having a fixed height and width
