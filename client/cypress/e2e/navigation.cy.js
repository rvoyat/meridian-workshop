describe('Navigation', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('loads the dashboard', () => {
    cy.get('.top-nav').should('be.visible')
    cy.get('.nav-tabs').should('be.visible')
  })

  it('navigates to Inventory', () => {
    cy.get('.nav-tabs').contains('Inventory').click()
    cy.url().should('include', '/inventory')
  })

  it('navigates to Orders', () => {
    cy.get('.nav-tabs').contains('Orders').click()
    cy.url().should('include', '/orders')
  })

  it('navigates to Finance', () => {
    cy.get('.nav-tabs').contains('Finance').click()
    cy.url().should('include', '/spending')
  })

  it('navigates to Demand Forecast', () => {
    cy.get('.nav-tabs').contains('Demand').click()
    cy.url().should('include', '/demand')
  })

  it('navigates to Reports', () => {
    cy.get('.nav-tabs').contains('Reports').click()
    cy.url().should('include', '/reports')
  })
})
