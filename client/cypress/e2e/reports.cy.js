describe('Reports', () => {
  beforeEach(() => {
    cy.visit('/reports')
  })

  it('loads the Reports page without errors', () => {
    cy.get('.main-content').should('be.visible')
    cy.get('.error').should('not.exist')
  })

  it('displays report content after loading', () => {
    cy.get('.loading', { timeout: 8000 }).should('not.exist')
    cy.get('.card, .stat-card').should('have.length.greaterThan', 0)
  })

  it('filter bar is visible', () => {
    cy.get('.filter-bar, [class*="filter"]').should('be.visible')
  })
})
