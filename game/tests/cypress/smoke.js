/// <reference types="cypress" />

/**
 * This test goes through a longer user story
 * trying to do almost everything a typical user would do.
 */
export const smokeTest = () => {
  cy.visit('localhost:8000/rapidrouter')

  cy.log('open Level 1')
  cy.get('[data-cy=episode1-title]').click()
  cy.get('[data-cy=level1-title]').click()
  cy.get('[data-cy=popup]').should('be.visible')
  cy.get('[data-cy=popup-title]').should("have.text", "Level 1")

  cy.log('close popup')
  cy.get('#play_button').click()
  cy.get('[data-cy=popup]').should('not.be.visible')

  cy.log('fail popup')
  cy.get('[data-cy=play-level-button]').click()
  cy.get('[data-cy=popup]').should('be.visible')
  cy.get('[data-cy=popup-title]').should("have.text", "Oh dear!")

  cy.log('complete level')
  cy.get('#try_again_button').click()
  cy.get('[data-cy=move-forward-arrow]').click()
  cy.wait(1000)
  cy.get('[data-cy=play-level-button]').click()
  cy.get('[data-cy=popup]').should('be.visible')
  cy.get('[data-cy=popup-title]').should("have.text", "You win!")

  cy.log('load next level')
  cy.get('#next_level_button').click()
  cy.get('[data-cy=popup]').should('be.visible')
  cy.get('[data-cy=popup-title]').should("have.text", "Level 2")
}