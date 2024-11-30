/**
 * Testing utils
 */
import { shallowMount } from "@vue/test-utils";

/**
 * Components
 */
import App from "@/components/HelloWorld.vue";

/**
 * Test Cases
 */
describe("HelloWorld", () => {
  /**
   * Test Case #1: Check if component is existing
   */
  describe("Existing", () => {
    const wrapper = shallowMount(App);

    /**
     * Component should be existing
     */
    test("True", () => {
      expect(wrapper.exists()).toBe(true);
    });
  });
});
