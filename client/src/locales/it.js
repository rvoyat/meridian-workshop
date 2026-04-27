export default {
  // Navigation
  nav: {
    overview: 'Panoramica',
    inventory: 'Inventario',
    orders: 'Ordini',
    finance: 'Finanze',
    demandForecast: 'Previsione della domanda',
    companyName: 'Catalyst Components',
    subtitle: 'Sistema di gestione inventario'
  },

  // Dashboard
  dashboard: {
    title: 'Panoramica',
    kpi: {
      title: 'Indicatori chiave di performance',
      inventoryTurnover: 'Tasso di rotazione inventario',
      ordersFulfilled: 'Ordini evasi',
      orderFillRate: 'Tasso di evasione ordini',
      revenue: 'Ricavi (ordini)',
      revenueYTD: 'Ricavi (ordini) da inizio anno',
      revenueMTD: 'Ricavi (ordini) da inizio mese',
      avgProcessingTime: 'Tempo medio di elaborazione (giorni)',
      goal: 'Obiettivo'
    },
    summary: {
      title: 'Riepilogo'
    },
    orderHealth: {
      title: 'Stato ordini',
      totalOrders: 'Totale ordini',
      revenue: 'Ricavi',
      avgOrderValue: 'Valore medio ordine',
      onTimeRate: 'Tasso di puntualità',
      avgFulfillmentDays: 'Evasione media (giorni)',
      total: 'Totale'
    },
    ordersByMonth: {
      title: 'Ordini per mese'
    },
    inventoryValue: {
      title: 'Valore inventario per categoria'
    },
    inventoryShortages: {
      title: 'Carenze inventario',
      noShortages: 'Nessuna carenza - tutti gli ordini possono essere evasi!',
      noData: 'Nessun dato inventario per i filtri selezionati',
      orderId: 'ID ordine',
      sku: 'SKU',
      itemName: 'Nome articolo',
      quantityNeeded: 'Quantità necessaria',
      quantityAvailable: 'Quantità disponibile',
      shortage: 'Carenza',
      daysDelayed: 'Giorni di ritardo',
      priority: 'Priorità',
      unitsShort: 'unità mancanti',
      days: 'giorni'
    },
    topProducts: {
      title: 'Prodotti principali per ricavi',
      sku: 'SKU',
      product: 'Prodotto',
      category: 'Categoria',
      warehouse: 'Magazzino',
      stockStatus: 'Stato scorte',
      revenue: 'Ricavi',
      unitsOrdered: 'Unità ordinate',
      firstOrder: 'Primo ordine',
      inStock: 'Disponibile',
      lowStock: 'Scorte basse'
    }
  },

  // Inventory
  inventory: {
    title: 'Inventario',
    description: 'Traccia e gestisci tutti gli articoli in inventario',
    stockLevels: 'Livelli di scorte',
    skus: 'SKU',
    searchPlaceholder: 'Cerca per nome articolo...',
    clearSearch: 'Cancella ricerca',
    totalItems: 'Totale articoli',
    totalValue: 'Valore totale',
    lowStockItems: 'Articoli con scorte basse',
    warehouses: 'Magazzini',
    table: {
      sku: 'SKU',
      itemName: 'Nome articolo',
      name: 'Nome',
      category: 'Categoria',
      warehouse: 'Magazzino',
      quantity: 'Quantità',
      quantityOnHand: 'Quantità disponibile',
      reorderPoint: 'Punto di riordino',
      unitCost: 'Costo unitario',
      unitPrice: 'Prezzo unitario',
      totalValue: 'Valore totale',
      location: 'Posizione',
      status: 'Stato'
    }
  },

  // Orders
  orders: {
    title: 'Ordini',
    description: 'Visualizza e gestisci gli ordini dei clienti',
    allOrders: 'Tutti gli ordini',
    totalOrders: 'Totale ordini',
    totalRevenue: 'Ricavi totali',
    avgOrderValue: 'Valore medio ordine',
    onTimeDelivery: 'Consegna puntuale',
    itemsCount: '{count} articoli',
    quantity: 'Qtà',
    table: {
      orderNumber: 'Numero ordine',
      orderId: 'ID ordine',
      orderDate: 'Data ordine',
      date: 'Data',
      customer: 'Cliente',
      category: 'Categoria',
      warehouse: 'Magazzino',
      items: 'Articoli',
      value: 'Valore',
      totalValue: 'Valore totale',
      status: 'Stato',
      expectedDelivery: 'Consegna prevista',
      actualDelivery: 'Consegna effettiva'
    }
  },

  // Finance/Spending
  finance: {
    title: 'Dashboard finanziario',
    description: 'Traccia ricavi, costi e performance finanziaria',
    totalRevenue: 'Ricavi totali',
    totalCosts: 'Costi totali',
    netProfit: 'Utile netto',
    avgOrderValue: 'Valore medio ordine',
    fromOrders: 'Da {count} ordini',
    costBreakdown: 'Approvvigionamento + Operativo + Personale + Spese generali',
    margin: 'margine',
    perOrderRevenue: 'Ricavo per ordine',
    revenueVsCosts: {
      title: 'Ricavi vs costi mensili',
      revenue: 'Ricavi',
      costs: 'Costi totali'
    },
    monthlyCostFlow: {
      title: 'Flusso costi mensile',
      procurement: 'Approvvigionamento',
      operational: 'Operativo',
      labor: 'Personale',
      overhead: 'Spese generali'
    },
    categorySpending: {
      title: 'Spesa per categoria',
      ofTotal: 'del totale'
    },
    transactions: {
      title: 'Transazioni recenti',
      id: 'ID',
      description: 'Descrizione',
      vendor: 'Fornitore',
      date: 'Data',
      amount: 'Importo'
    }
  },

  // Demand Forecast
  demand: {
    title: 'Previsione della domanda',
    description: 'Analizza le tendenze della domanda e le previsioni',
    increasingDemand: 'Domanda crescente',
    stableDemand: 'Domanda stabile',
    decreasingDemand: 'Domanda in calo',
    itemsCount: '{count} articoli',
    more: 'altro...',
    demandForecasts: 'Previsioni della domanda',
    table: {
      sku: 'SKU',
      itemName: 'Nome articolo',
      currentDemand: 'Domanda attuale',
      forecastedDemand: 'Domanda prevista',
      change: 'Variazione',
      trend: 'Tendenza',
      period: 'Periodo'
    }
  },

  // Reports
  reports: {
    title: 'Report di performance',
    description: 'Visualizza le metriche trimestrali e le tendenze mensili',
    quarterly: {
      title: 'Performance trimestrale',
      quarter: 'Trimestre',
      totalOrders: 'Totale ordini',
      totalRevenue: 'Ricavi totali',
      avgOrderValue: 'Valore medio ordine',
      fulfillmentRate: 'Tasso di evasione'
    },
    monthlyTrend: {
      title: 'Andamento ricavi mensili'
    },
    monthlyAnalysis: {
      title: 'Analisi mese su mese',
      month: 'Mese',
      orders: 'Ordini',
      revenue: 'Ricavi',
      change: 'Variazione',
      growthRate: 'Tasso di crescita'
    },
    stats: {
      totalRevenueYTD: 'Ricavi totali (da inizio anno)',
      avgMonthlyRevenue: 'Ricavi medi mensili',
      totalOrdersYTD: 'Totale ordini (da inizio anno)',
      bestQuarter: 'Miglior trimestre'
    }
  },

  // Filters
  filters: {
    timePeriod: 'Periodo',
    location: 'Posizione',
    category: 'Categoria',
    orderStatus: 'Stato ordine',
    all: 'Tutti',
    allMonths: 'Tutti i mesi'
  },

  // Statuses
  status: {
    delivered: 'Consegnato',
    shipped: 'Spedito',
    processing: 'In elaborazione',
    backordered: 'In attesa',
    inStock: 'Disponibile',
    lowStock: 'Scorte basse',
    adequate: 'Adeguato'
  },

  // Trends
  trends: {
    increasing: 'crescente',
    stable: 'stabile',
    decreasing: 'in calo'
  },

  // Priority
  priority: {
    high: 'Alta',
    medium: 'Media',
    low: 'Bassa'
  },

  // Categories
  categories: {
    circuitBoards: 'Schede elettroniche',
    sensors: 'Sensori',
    actuators: 'Attuatori',
    controllers: 'Controllori',
    powerSupplies: 'Alimentatori'
  },

  // Spending Categories
  spendingCategories: {
    rawMaterials: 'Materie prime',
    components: 'Componenti',
    equipment: 'Attrezzature',
    consumables: 'Materiali di consumo'
  },

  // Warehouses
  warehouses: {
    sanFrancisco: 'San Francisco',
    london: 'Londra',
    tokyo: 'Tokyo'
  },

  // Months
  months: {
    jan: 'Gen',
    feb: 'Feb',
    mar: 'Mar',
    apr: 'Apr',
    may: 'Mag',
    jun: 'Giu',
    jul: 'Lug',
    aug: 'Ago',
    sep: 'Set',
    oct: 'Ott',
    nov: 'Nov',
    dec: 'Dic',
    january: 'Gennaio',
    february: 'Febbraio',
    march: 'Marzo',
    april: 'Aprile',
    june: 'Giugno',
    july: 'Luglio',
    august: 'Agosto',
    september: 'Settembre',
    october: 'Ottobre',
    november: 'Novembre',
    december: 'Dicembre'
  },

  // Profile Menu
  profile: {
    profileDetails: 'Dettagli profilo',
    myTasks: 'Le mie attività',
    logout: 'Disconnetti'
  },

  // Profile Details Modal
  profileDetails: {
    title: 'Dettagli profilo',
    email: 'Email',
    department: 'Dipartimento',
    location: 'Sede',
    phone: 'Telefono',
    joinDate: 'Data di assunzione',
    employeeId: 'Matricola',
    close: 'Chiudi'
  },

  // Tasks Modal
  tasks: {
    title: 'Le mie attività',
    taskTitle: 'Titolo attività',
    taskTitlePlaceholder: 'Inserisci titolo attività...',
    priority: 'Priorità',
    dueDate: 'Scadenza',
    addTask: 'Aggiungi attività',
    noTasks: 'Nessuna attività. Aggiungi la tua prima attività in alto!'
  },

  // Language
  language: {
    english: 'Inglese',
    japanese: 'Giapponese',
    italian: 'Italiano',
    selectLanguage: 'Seleziona lingua'
  },

  // Common
  common: {
    loading: 'Caricamento...',
    error: 'Errore',
    noData: 'Nessun dato disponibile',
    viewDetails: 'Visualizza dettagli',
    close: 'Chiudi',
    save: 'Salva',
    cancel: 'Annulla',
    search: 'Cerca',
    filter: 'Filtra',
    export: 'Esporta',
    items: 'articoli'
  }
}
