/// <reference types="cypress" />

import { smokeTest } from './smoke'

it('does not smoke', () => {
  smokeTest()
})