import { smokeTest } from './smoke'

Cypress._.each(['macbook-15', 'iphone-6'], viewport => {
  it(`works on ${viewport}`, () => {
    cy.viewport(viewport)
    smokeTest()
  })
})