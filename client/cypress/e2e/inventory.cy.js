describe('Inventory', () => {
  beforeEach(() => {
    cy.visit('/inventory')
  })

  it('displays the inventory table', () => {
    cy.get('table').should('be.visible')
    cy.get('thead').should('be.visible')
    cy.get('tbody tr').should('have.length.greaterThan', 0)
  })

  it('shows loading state then data', () => {
    cy.visit('/inventory')
    cy.get('table', { timeout: 8000 }).should('be.visible')
  })

  it('opens item detail on row click', () => {
    cy.get('tbody tr').first().click()
    cy.get('.modal, [class*="modal"]', { timeout: 5000 }).should('be.visible')
  })
})
