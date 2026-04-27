import { ref, computed } from 'vue'

const savedTheme = localStorage.getItem('app-theme') || 'light'
const isDark = ref(savedTheme === 'dark')

document.documentElement.setAttribute('data-theme', savedTheme)

export function useTheme() {
  const toggleTheme = () => {
    isDark.value = !isDark.value
    const theme = isDark.value ? 'dark' : 'light'
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('app-theme', theme)
  }

  return { isDark: computed(() => isDark.value), toggleTheme }
}
